# Sample dict of the gen ed categories and corresponding courses
genEdCategories = {"Creativity and Innovation" : ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330"],
                   "Communication and Expression": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"],
                   "Equity, Diversity, and Inclusion": ["ART-450", "ENG-214", "ES-220", "GSWS-312","MUS-205"],
                   "Inquiry and Analysis": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482"],
                   "Numerical Literacy": ["CS-200", "MTH-111", "CS-346", "STAT-243z"],
                   "Purposeful Learning": ["WR-121z","WR-122z", "WR-123"],
                   "Uncategorized": []}

# Sample transcript of unorganized courses
transcript = ( "    MTH-111, Pre-calculus, 4, COMPLETED    ",
    "  WR-121z, Composition I, 3, Completed   ",
    "  WR-122z,  Composition II, 3, Incomplete   ",
    "     GSWS-210, Violence Prevention, 4, completed")


"""---------------------------------------------^^^ Samples above ^^^^----------------------------------------------------"""
"""---------------------------------------------Functions Below vvvvvv----------------------------------------------------"""


def parseCourseRecord(courseString):
    """ 
    This function will format a single course string into a structured dict. 
    
    Parameter:
    courseString (str): A string of unorganized course information
    
    Returns:
    a dict: keys of "code", "name", "credits", and "status" and values are the corresponding information from the parameters.
    """
    courseString = courseString.strip()
    courseList = courseString.split(",")
    courseDict = {"code": courseList[0].strip().upper(), "name": courseList[1].strip(), "credits": int(courseList[2].strip()), "status": courseList[3].strip().upper()}
    return courseDict
    
    
"""---------------------------------------------Break Line For Clarity----------------------------------------------------"""    

    
def main(genEdCategories, transcript):
    """ 
    Runs tests at the moment.
    
    Parameters:
    genEdCategories (dict): A sample dict of gen ed categories and corresponding course titles
    transcript (tuple): A sample transcript of unorganized course strings
    
    No returns
    """
    # Initialize empty list to hold parsed courses
    parsedCourse = []
    
    # Loop though each course and parse
    for course in transcript:
        parsedCourse.append(parseCourseRecord(course))
    
    #print for testing
    print(parsedCourse)

main(genEdCategories, transcript)