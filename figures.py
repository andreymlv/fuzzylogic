

class Triangle():

    def __init__(self, lower, upper, peak, x):
        self.lower = lower
        self.upper = upper
        self. peak = peak
        self.x = x

        self.a = self.upper - self.lower
        self.u = self.mftriangle()
    
    def mftriangle(self):
        u = 0
        if ((self.x >= self.lower) and (self.x <= self.peak)):
            u = 1 - ((self.peak - self.x) / (self.peak - self.lower))
            return u
        if ((self.x >= self.peak) and (self.x <= self.upper)):
            u = 1 - ((self.x - self.peak) / (self.upper - self.peak))
            return u
        return u

    def get_coords(self):    

        print(self.u)
        
        """
        everywhere add by +a*i
        x_list = [self.lower, self.lower+self.upper-x[i], x[i], self.upper]
        y_list = [0, u, u, 0]
        """

        if (self.u != 1.0):
            x_list = sorted([self.lower, self.lower+self.upper-self.x, self.x, self.upper])
            y_list = [0, self.u, self.u, 0]
        else:
            x_list = sorted([self.lower, self.x, self.upper])
            y_list = [0, self.u, 0]

        coords = list()
        coords.append(x_list)
        coords.append(y_list)

        return coords

    
    def make_plots(self):
        if (self.u == 1):
            plt.plot([lower+a*i, x[i]+a*i, upper+a*i], [0, 1, 0])
        else:
            plt.plot(sorted(x_list), y_list)


class Trapezoid():

    def __init__(self, lower, upper, first_peak, second_peak, x):
        pass

    def mftrapezoid(self):
        u = 0
        if ((x >= lower) and (x <= peak_lower)):
            u = 1 - ((peak_lower - x) / (peak_lower - lower))
            return u
        if (x >= peak_lower) and (x <= peak_upper):
            u = 1
            return u
        if ((x >= peak_upper) and (x <= upper)):
            u = 1 - ((x - peak_upper) / (upper - peak_upper))
            return u
        return u

    def get_coords(self):
        pass