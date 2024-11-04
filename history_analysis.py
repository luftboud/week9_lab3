"""A module for work with chrome history"""

def sites_on_date(visits: list, date: str)-> set[str]:
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in the browser history
    (you get it as the result of the function get_chrome_os
    from get_browser_history module)
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    """
    url_set = set()
    for el in visits:
        if el[2] == date:
            url_set.add(el[0])
    return url_set


def most_frequent_sites(visits: list, number: int)-> set[str]:
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    If the frequence is the same choose sites in the alphabetical order
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> visits = get_chrome_os("ija","MacOS")
    >>> print(most_frequent_sites(visits,5))
    """
    list_of_sites = [el[0] for el in visits]
    set_of_sites = set(list_of_sites)
    frequency = []
    for el in set_of_sites:
        num = list_of_sites.count(el)
        frequency.append((num,el))
    frequency = sorted(frequency)
    def determine_frequency(item):
        """A func used for sorting according to frequency"""
        return item[0]
    frequency = sorted(frequency, key=determine_frequency, reverse=True)
    frequency = frequency[:number]
    return {el[1] for el in frequency}


def get_url_info(visits: list, url: str)->tuple:
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    """
    title = None
    visit_dates = []
    visit_times = []
    num_of_visits = 0
    visit_durations = []
    for el in visits:
        if el[0] == url:
            title = el[1]
            num_of_visits +=1
            visit_dates.append(el[2])
            visit_durations.append(el[4])
    if title is None:
        return ("", "", "", 0, 0)
    for el in visits:
        if el[0] == url and el[2] == max(visit_dates):
            visit_times.append(el[3])
    average_time = 0
    if len(visit_durations) != 0:
        average_time = sum(visit_durations) / len(visit_durations)
    return title, max(visit_dates), max(visit_times), num_of_visits, average_time

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
