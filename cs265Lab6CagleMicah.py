# Sample dict of the gen ed categories and corresponding courses
genEdCategories = {"Creativity and Innovation" : ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330"],
                   "Communication and Expression": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"],
                   "Equity, Diversity, and Inclusion": ["ART-450", "ENG-214", "ES-220", "GSWS-312","MUS-205"],
                   "Inquiry and Analysis": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482"],
                   "Numerical Literacy": ["CS-200", "MTH-111", "CS-346", "STAT-243z"],
                   "Purposeful Learning": ["WR-121Z","WR-122Z", "WR-123"],
                   "Uncategorized": []}

# Sample transcript of unorganized courses
transcript = ( "    MTH-111, Pre-calculus, 4, COMPLETED    ",
    "  WR-121z, Composition I, 3, Completed   ",
    "  WR-122z,  Composition II, 3, incomplete   ",
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


def getGenEdCategory(courseCode, genEdMapping):
    """
    This function will determine which Gen Ed category a course belongs to. 
    
    Parameters:
    courseCode (str): the parsed course code from the transcript.
    genEdMapping (dict): a dict of gen ed categories and corresponding course titles.
    
    Returns:
    The category name (str)
    """
    
    for category, course in genEdMapping.items():
        if courseCode in course:
            return category
        else:
            continue


"""---------------------------------------------Break Line For Clarity----------------------------------------------------"""


def auditCredits(studentBins):
    """
    This function will calculate total completed credits per Gen Ed category using the studentBins. 
    
    Parameter:
    studentBins (dict): keys: (str) Gen Ed category names (+uncategorized) and values: (list) course dicts containging keys:"code", "name", "credits", and "status".
    
    Returns:
    A dict with keys as Gen Ed category names and values as the total completed credits for each category.
    """
    # Initialize dict to hold total completed credits per category
    completedCredits = {"Creativity and Innovation" : 0,
                   "Communication and Expression": 0,
                   "Equity, Diversity, and Inclusion": 0,
                   "Inquiry and Analysis": 0,
                   "Numerical Literacy": 0,
                   "Purposeful Learning": 0,
                   "Uncategorized": 0}
    # Loop through each category and calculate total completed credits
    for category, courses in studentBins.items():
        totalCredits = 0
        for course in courses:
            if course["status"] == "COMPLETED":
                totalCredits += course["credits"]
                completedCredits[category] = totalCredits
            else:
                completedCredits[category] = totalCredits
                
    return completedCredits


"""---------------------------------------------Break Line For Clarity----------------------------------------------------"""


def binStudentCourses(transcript, genEdMap): # 
    """
    This function will group completed courses into lists under their respective Gen Ed category keys.
    
    Parameters:
    transcript (list of dicts): The parsed course record of the student where the items are dicts: keys: identifers, values: corresponding identifiers
    genEdMapping (dict): keys: categories, values: list of courses corresponding to the category
    
    Returns:
    A dict where keys: Ged Ed categories, values: lists are ("course code (str)", "credits (int)")
    """
    #Initialize dict
    binnedDict = {"Creativity and Innovation" : [],
                   "Communication and Expression": [],
                   "Equity, Diversity, and Inclusion": [],
                   "Inquiry and Analysis": [],
                   "Numerical Literacy": [],
                   "Purposeful Learning": [],
                   "Uncategorized": []}
    #Initialize Parsed Courses List
    parsedCourse = []
    #Loop through each course, parse and put in designated bin
    for string in transcript:
        parsedCourse.append(parseCourseRecord(string))
    for course in parsedCourse:
        if course["status"] == "COMPLETED":
            category = getGenEdCategory(course["code"], genEdMap)
            courseCodeAndCredits = (course["code"], course["credits"])
            binnedDict[category].append(courseCodeAndCredits)
            
    return binnedDict
        
        
        
    


"""---------------------------------------------Break Line For Clarity----------------------------------------------------"""


    
def main(genEdCategories, transcript):
    """ 
    Runs tests at the moment.
    
    Parameters: (for testing, not sure if needed for final submission)
    genEdCategories (dict): A sample dict of gen ed categories and corresponding course titles
    transcript (tuple): A sample transcript of unorganized course strings
    
    No returns
    """
    # # Initialize empty list to hold parsed courses
    # parsedCourse = []
    # # Loop though each course and parse
    # for course in transcript:
    #     parsedCourse.append(parseCourseRecord(course))
        
    # #print for testing
    # print(parsedCourse)
    
    
    
    
    # # Initialize empty dict to hold courses organized by category
    # categorizedCourses = {}
    # # Loop through each course and determine the gen ed category
    # for course in parsedCourse:
    #     category = getGenEdCategory(course["code"], genEdCategories)
    #     if category is None:
    #         category = "Uncategorized"
        
        # # Print the course code for testing purposes
        # print(f"Course Code: {course['code']}, Category: {category}")
        
    #     # Puts each course into a dict with the key as the category and the value as a list of courses in that category
    #     if category not in categorizedCourses:
    #         categorizedCourses[category] = []
    #         categorizedCourses[category].append(course)

    #     else:
    #         categorizedCourses[category].append(course)
        
    # # # Print the categorized courses for testing purposes
    # # print(categorizedCourses)
    
    
    # # Audit Credits (printed for testing)
    # print(auditCredits(categorizedCourses))
    
    
    #print the function for testing
    print(binStudentCourses(transcript, genEdCategories))


main(genEdCategories, transcript)