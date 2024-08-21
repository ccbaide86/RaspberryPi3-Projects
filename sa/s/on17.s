.global _start

.section .data
msg_wiringPi_fail:
    .asciz "No se pudo inicializar WiringPi\n"
msg_encendido:
    .asciz "Encendido\n"
msg_error_file:
    .asciz "<<< ERROR EN EL ARCHIVO >>>\n"
file_path:
    .asciz "/home/sa/raspberry/estado17.txt"
format_string:
    .asciz "%d\n"

.section .bss
    .lcomm buffer, 1024

.section .text

_start:
    // Llamar a wiringPiSetup()
    bl wiringPiSetup
    cmp r0, #0
    bne wiringpi_fail

    // Configurar el pin como OUTPUT
    ldr r0, =0          // pin = 0
    mov r1, #1          // OUTPUT
    bl pinMode          // pinMode(pin, OUTPUT)

    // Establecer el pin en HIGH
    ldr r0, =0          // pin = 0
    mov r1, #1          // HIGH
    bl digitalWrite     // digitalWrite(pin, HIGH)

    // Esperar 1 segundo
    bl delay_1s

    // Imprimir mensaje "Encendido\n"
    ldr r0, =msg_encendido
    bl printf

    // Abrir archivo para escribir
    ldr r0, =file_path
    ldr r1, =file_write_mode
    bl fopen
    cmp r0, #0
    beq file_error

    // Escribir "1" en el archivo
    mov r1, r0          // Guardar el puntero del archivo en r1
    ldr r0, =format_string
    mov r2, #1          // Valor a escribir en el archivo
    bl fprintf          // fprintf(pf, "%d", 1)

    // Escribir un salto de línea
    mov r0, r1          // Puntero al archivo
    ldr r1, =newline
    bl fputs            // fputs("\n", pf)

    // Cerrar el archivo
    mov r0, r1
    bl fclose
    b cleanup

wiringpi_fail:
    // Error al inicializar wiringPi
    ldr r0, =msg_wiringPi_fail
    bl puts
    b cleanup

file_error:
    // Error al abrir archivo
    ldr r0, =msg_error_file
    bl puts
    b cleanup

cleanup:
    mov r7, #1          // syscall: exit
    svc #0

delay_1s:
    mov r0, #1000       // 1000 ms
    bl delay
    bx lr               // Volver a la función anterior

.section .data
file_write_mode:
    .asciz "w"
newline:
    .asciz "\n"
