import statsmodels.stats.proportion
from typing import Tuple, Union

def calc_confidence(num: int, denom: int, alpha: int = 0.05, combined: bool = True) -> Union[str,Tuple[str,str,str]]:
    """
    outputs a three line string with a proportion, percentage, and confidence interval for each cell. Confidence interval is calculated using the agresti coull method.
    Summation occurs by row, and must be transposed prior to use if column summation is required
    :param num: numerator value
    :param denom: denominator value
    :param alpha: alpha value for confidence interval. default .05 to calculate 95% confidence
    :param combine: True by default, wraps the output in an excel readable string. False splits the output into 3
    seperate variables.
    :return: string with carriage returns to be read by excel if combined == True.
    3 seperate strings for proportion, percent, CI if combined == False.
    """
    if denom == 0:
        return "0"
    raw_ci = statsmodels.stats.proportion.proportion_confint(num, denom, alpha, method="agresti_coull")
    CI = f"({raw_ci[0] * 100:.1f} - {raw_ci[1] * 100:.1f})"
    percent = f"{(num/denom)*100:.1f}%"
    proportion = f"{num}/{denom}"
    if combined is True:
        return f'"{proportion}\n{percent}\n{CI}"'
    else:
        return proportion, percent, CI

