class PID:
    """
    Implement an PID Controller
    """
    def __init__(self, target, kp, ki, kd) -> None:
        self.target = target
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error = 0
        self.last_error = 0
        self.d_error = 0
        self.i_error = 0
        self.i_error_limit = 5

    def update_controller(self, error):
        self.error = error
        

    def control_value(self, process_variable):
        self.error = self.target - process_variable
        self.d_error = self.error - self.last_error
        self.i_error += self.error
        self.last_error = self.error

        if self.i_error > self.i_error_limit:
            self.i_error = self.i_error_limit
        elif self.i_error <-self.i_error_limit:
            self.i_error = -self.i_error_limit

        control_value = self.error*self.kp + self.d_error*self.kd + self.i_error*self.ki

        return control_value