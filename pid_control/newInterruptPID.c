#include "variables.h";

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef* htim)
{
	//declaration of temporary variables
	float uPid = 0.0, derivative, P, I, D;
	//measurment of object
	BMP280_ReadTemperatureAndPressure(&temperature, &pressure);
	//simple error calculations
	error = desired_temperature - temperature;
	integralError += error;
	derivative = (error - previousError)/dt;
	//PID callculations according to "wykład 7"
	P = Kp * error;
	I = Ki * integralError*(dt/2.0);
	D = Kd * derivative;
	//u callculation
	uPid = P + I + D;
	//Saturation
	if(uPid > 1.0)
	{
		uPid = 1.0;
	}
	if(uPid < 0.0)
	{
		uPid = 0.0;
	}
	//u to DUTY conversion
	pwm_duty = uPid * 1000;
	//u output
	__HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_3, pwm_duty);
	//logging output
	snprintf(text, sizeof(text), "{\"temperature\":%.2f,\"control\":%.2f,\"desired\":%.2f}\n", temperature, desired_temperature, pwm_duty);
	HAL_UART_Transmit(&huart3, (uint8_t*)text, strlen(text), 1000);
	text[0] = 0;
	//changing last 
	previousError = error
}
