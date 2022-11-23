class Course:
    def __init__(self, name, prereqs, units):
        self.name = name;
        self.prereqs = prereqs
        self.units = units

class Schedule:
    def __init__(self, num_terms, max_units_per_term, num_years = 4, has_summer = True, max_units_summer = None):
        self.num_terms = num_terms
        self.max_units_per_term = max_units_per_term
        self.num_years = num_years
        self.has_summer = has_summer
        if self.has_summer and max_units_summer is None:
            raise ValueError("If summer is true, you must specify maxUnitsSummer")
        self.maxUnitsSummer = max_units_summer

        self.term_settings = dict(
            max_units_per_term=max_units_per_term
        )

        if self.has_summer:
            self.summer_term_settings = dict(
                max_units_per_term=max_units_summer
            )

        self.years =  [
            {
                term + 1: self._create_empty_term(self.term_settings)
                for term in range(num_terms)
            } |
            (
                {
                    "S": self._create_empty_term(self.summer_term_settings)
                } if has_summer else {}
            )
            for year in range(num_years)
        ]
    
    def _create_empty_term(self, term_settings):
        return dict(
            term_settings = term_settings
        )
    
    def get_term(self, year, term):
        if isinstance(term, int):
            # if term is one out of range, assume it is summer
            if term == self.num_terms + 1 and self.has_summer:
                term = "S"
            elif term > self.num_terms:
                raise ValueError("num_terms out of range")
            
        


schedule = Schedule(
    num_terms = 3,
    max_units_per_perm = 19,
    has_summer = True,
    max_units_summer = 18
)
print(schedule.years)