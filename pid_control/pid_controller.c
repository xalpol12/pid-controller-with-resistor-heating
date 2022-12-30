#include <stdio.h>
#include <stdint.h>

typedef float float32_t;

typedef struct{
	float32_t Kp;
	float32_t Ki;
	float32_t Kd;
	float32_t dt;
}pid_parameters_t;

typedef struct{
	pid_parameters_t p;
	float32_t previous_error, previous_integral;	
}pid_t;


/**
* Calculation of discrete PID
* @param[in,out] s A pointer to PID parameters and history
* @param[in] setpoint Input setpoint value
* @param[in] measured Input measured value
* @return PID output value
*/
float32_t calculate_discrete_pid(pid_t* pid, float32_t setpoint, float32_t measured){
	float32_t u=0, P, I, D, error, integral, derivative;
	
	error = setpoint-measured;
	
	//proportional part
	P = pid->p.Kp * error;

	//integral part
	integral = pid->previous_integral + (error+pid->previous_error) ; //numerical integrator without anti-windup
	pid->previous_integral = integral;
	I = pid->p.Ki*integral*(pid->p.dt/2.0);

	//derivative part
	derivative = (error - pid->previous_error)/pid->p.dt; //numerical derivative without filter
	pid->previous_error = error;
	D = pid->p.Kd*derivative;
	
	//sum of all parts
	u = P  + I + D; //without saturation
	
	return u;
}


int main() {
	uint16_t number_of_samples=1000;
	float32_t dt=1, setpoint=26.0, measured=0, pid_output;
    pid_t pid1 = { .p.Kp=0.93, .p.Ki=0.0039, .p.Kd=0, .p.dt=dt, .previous_error=0, .previous_integral=0};
    
    while(number_of_samples--)
    {
		measured = 0.0; //pass current value to measured in this line!
		pid_output = calculate_discrete_pid(&pid1, setpoint, measured);
    }
    return 0;
}
  