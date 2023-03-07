function [t,theta,complexform,order] = setup_kuramoto(N,w,K,tspan)

    thetaI = (1:N)'/N*2*pi; % Initial phase starts uniform around unit circle
    [t,theta] = ode45(@ode,tspan,thetaI);
    complexform = exp(1i*theta); 
    order = abs(1/N*sum(exp(1i*theta),2))
    
        function theta_dot = ode(~,theta)
            theta_dot = w + K/N*sum(sin(theta-theta'))';
        end
end
