#include <stdio.h>
#include <stdint.h>
#include <math.h>

typedef float float32_t;

typedef struct{
	float32_t H;
	float32_t u_min, u_max;
	float32_t u_value;	
}two_position_t;


/**
* Calculation of two-position controller
* @param[in,out] s A pointer to two-position controller parameters and history
* @param[in] setpoint Input setpoint value
* @param[in] measured Input measured value
* @return Controller output value
*/
float32_t calculate_two_position_controller(two_position_t* controller, float32_t setpoint, float32_t measured){
	float32_t error;
	
	error = setpoint-measured;
	//Controller
	if(error >= controller->H/2.0) controller->u_value = controller->u_max;
	else if(error < -1*controller->H/2.0) controller->u_value = controller->u_min;
	return controller->u_value;
}


int main() {
	uint16_t number_of_samples=1000;
	float32_t t=0, dt=1, setpoint=, measured=0, controller_output;
    two_position_t tp1 = { .H=0.5, .u_min=0, .u_max=1.0, .u_value=0};

    while(number_of_samples--)
    {
		setpoint = 4*sin(2.0*3.14*0.25*t); //0.25 Hz sin
		measured = 0.0;
		t=t+dt;
		controller_output = calculate_two_position_controller(&tp1, setpoint, measured);
    }
    return 0;
}
  