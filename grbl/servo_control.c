/*
 * servo_control.c
 *
 * Created: 12/1/2019 2:47:44 PM
 *  Author: dmay3
 */ 
#include "grbl.h"

void servo_init()
{
	SERVO_PWM_DDR |= (1<<SERVO_PWM_YBIT) | (1<<SERVO_PWM_ZBIT); // Configure as PWM output pin.
	SERVO2_PWM_DDR |= (1<<SERVO_PWM_YBIT) | (1<<SERVO_PWM_ZBIT); // Configure as PWM output pin.
	
	//Set for fast PWM using compare A and B registers
	TCCRA_REGISTER = (1<<5) | (1<<COMA_BIT) | (1<<WAVE1_REGISTER) | (1<<WAVE0_REGISTER);
	TCCRB_REGISTER = (TCCRB_REGISTER & 0b11111000) | 0x07; // set to 1/1024 Prescaler
	
	SERVO_OCRY = 9;
	SERVO_OCRZ = 1 ;
	
}