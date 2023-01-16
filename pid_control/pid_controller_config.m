clc; clear all; close all;

%model
input_amplitude = 0.9;
set_point = 27.5;

s = tf('s');
k = 11/input_amplitude; %model gain -> modify
T = 250; %model time constant -> modify
delay = 10; %model delay -> modify
H = k/(1+s*T)*exp(-s*delay); %model

%controller params
dt = 1;
kp = 0.607338773069937;
ki = 0.00245637321622817;
kd = 0;

%plotting variables
system_offset = 25;