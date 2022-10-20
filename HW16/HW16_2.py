class Mathematician:
    
    def square_nums(self, numbers:list):
        result = []
        for number in numbers:
            result.append(number*number)
        return result
    
    def remove_positives(self, numbers:list):
        result = []
        for number in numbers:
            if number < 0:
                result.append(number)
        return result
    
    def filter_leaps(self, years:list):
        result = []
        for year in years:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                result.append(year)
        return result
