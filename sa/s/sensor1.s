.global _start

.section .data
msg_wiringPi_fail:
    .asciz "No se pudo inicializar WiringPi\n"
msg_ready:
    .asciz "Listo para comenzar!\n"
msg_motion_detected:
    .asciz "Atención, se ha detectado movimiento %d\n"
script_off:
    .asciz "sudo /./home/sa/s/off21s"
script_on:
    .asciz "sudo /./home/sa/s/on21s"

.section .bss
    .lcomm buffer, 1024

.section .text

_start:
    // Variables locales
    mov r4, #0          // status0 = 0
    mov r5, #0          // status1 = 0
    mov r6, #0          // num = 0

    // Llamar a wiringPiSetup()
    bl wiringPiSetup
    cmp r0, #0
    bne wiringpi_fail

    // Configurar el pin como entrada
    mov r0, #1          // GPIO_PIR = 1
    mov r1, #0          // INPUT = 0
    bl pinMode          // pinMode(GPIO_PIR, INPUT)

    // Imprimir mensaje "Listo para comenzar!"
    ldr r0, =msg_ready
    bl printf

loop:
    // Leer estado del pin
    mov r0, #1          // GPIO_PIR = 1
    bl digitalRead
    mov r4, r0          // status0 = digitalRead(GPIO_PIR)

    // Verificar si se ha detectado movimiento
    cmp r4, #1
    bne no_motion
    cmp r5, #0
    bne no_motion
    add r6, r6, #1      // num++
    
    // Imprimir mensaje de movimiento detectado
    ldr r0, =msg_motion_detected
    mov r1, r6          // Pasar num como argumento
    bl printf
    
    // Ejecutar script para apagar
    ldr r0, =script_off
    bl system
    
    // Actualizar status1
    mov r5, #1

no_motion:
    cmp r4, #0
    bne sleep
    
    cmp r5, #1
    bne sleep
    
    // Imprimir mensaje "Listo para comenzar!"
    ldr r0, =msg_ready
    bl printf
    
    // Ejecutar script para encender
    ldr r0, =script_on
    bl system
    
    // Actualizar status1
    mov r5, #0

sleep:
    // Dormir 100 ms
    mov r0, #100000       // 100000 microsegundos (100 ms)
    bl usleep
    
    b loop

wiringpi_fail:
    // Error al inicializar wiringPi
    ldr r0, =msg_wiringPi_fail
    bl puts
    b cleanup

cleanup:
    mov r7, #1          // syscall: exit
    svc #0
