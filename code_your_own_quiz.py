# A program that presents a quiz to the user, prompts for & evaluates inputs,
# and outputs the result

quiz_blanks = ["__1__","__2__","__3__","__4__","__5__"]
quiz_answers = ["blanks,three,easy,medium,hard","NCAA,March,64,Elite,Four","1991,yellow,"
    "multi-paradigm,def,:"]
intro = "Please select a quiz difficulty by typing in one of the below options: "
quiz = ["This is quiz 1. It is easy. It has __1__ to fill in. There are __2__ quizzes available "
        "to choose from. This one is __3__ in difficulty, while the other options are __4__ and "
        "__5__ .",
        "This is quiz 2. It is medium. March Madness is a tournament put on by the __1__ . "
        "It happens every __2__ and April. The tournament is made up of 68 teams, but only "
        "__3__ actually officially make it into the tournament. There are 6 rounds of the "
        "tournament: the round of 64, round of 32, sweet 16, __4__ 8, Final __5__ , and the "
        "national championship.",
        "This is quiz 3. It is hard. Python is a programming langauge that first showed up in "
        "__1__ . Its logo is made up of two pythons, one blue in color, the other is __2__ . "
        "The lanaguage is very easy to learn compared to many other languages. It is a __3__ "
        "programming language, supporting, among other things, object-oriented programming and "
        "structured programming. Methods, or functions, are started with the __4__ identifier, "
        "which is then followed with a __5__ ."]
num_of_tries = 5


def start_quiz():
    """Initiates the program and processes the version of the quiz to execute."""
    version = 4
    while version > 3:
        print intro
        #difficulty = raw_input("Possible choices: 1 = easy, 2 = medium, 3 = hard: ")
        difficulty = raw_input("Possible choices: easy, medium, hard: ")
        version = quiz_version(difficulty)
        #i = version
        num_of_tries = int(raw_input("Enter max number of tries per blank you'd like to have: "))
    run_quiz(quiz, quiz_blanks, quiz_answers, version, num_of_tries)


def quiz_version(difficulty):
    """
    Checks user input to determine quiz version.

    Args:
        difficulty -- the input provided by the user
    Returns:
        version -- int value that tells program what version of quiz to run
    """
    version = 0
    if difficulty == 'easy':
        version = 1
        return int(version)
    elif difficulty == 'medium':
        version = 2
        return int(version)
    elif difficulty == 'hard':
        version = 3
        return int(version)
    else:
        print "Invalid Selection. Please try again."
        version = 4
        return int(version)


def run_quiz(quiz, quiz_blanks, quiz_answers, version, num_of_tries):
    """
    Runs the quiz process.

    Args:
        quiz -- quiz strings passed into the function
        quiz_blanks -- quiz blanks passed into the function
        quiz_answers -- quiz answers passed into the function
        version -- quiz version passed into the function
        num_of_tries -- number of tries, as previously input by the user
    Returns:
        none
    Prints:
        replaced -- final string with replaced answers
        
    """
    replaced = []
    print quiz[version-1]
    quiz = quiz[version-1].split()
    quiz_answers = quiz_answers[version-1].split(",")
  
    for word in quiz:
        replacement_needed = replacement_check(word, quiz_blanks, replaced)
        if replacement_needed != None:
            answer = answer_input(replacement_needed, quiz_blanks, quiz_answers, num_of_tries)
            if answer != "You've reached the max attempts. Please try the quiz again.":
                word = word.replace(replacement_needed, answer)
                replaced.append(word)
            else:
                print "fail: " + answer
                break
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print "Final: " + str(replaced)


def replacement_check(word, quiz_blanks, replaced):
    """
    Checks each word in the quiz string to determine if it needs to be replaced by user input.

    Args:
        word -- individual word from the active quiz list, to be checked
        quiz_blanks -- individual cross checker to determine when a word in the quiz needs replacement
        replaced -- updated quiz output list passed in, to then be passed into 'join_split' function
    Returns:
        word -- the cross check output, if relevant, such as '__1__', to prompt user which blank they are on
    """
    for prompts in quiz_blanks:
        if prompts in word:
            join_split(replaced, prompts)
            return word
    return None


def join_split(replaced, prompts):
    """
    Joins the list that makes up the quizzes current position, outputs it, then breaks back it down to a list
    for evaluation.

    Args:
        replaced -- current quiz replacement list
        prompts -- the 'quiz_blank' label that tells the user which prompt they are at, such as '__1__'
    Returns:
        replaced -- updated quiz replacement list
    """
    replaced = " ".join(replaced)
    print replaced + " " + prompts
    replaced = replaced.split()
    return replaced


def answer_input(replacement_needed, quiz_blanks, quiz_answers, num_of_tries):
    """
    Prompts the user for replacement input for the current blank in the quiz.

    Args:
        replacement_needed -- the 'quiz_blank' label that is currently being replaced
        quiz_blanks -- the 'quiz_blank' list used to determine location index to be replaced
        quiz_answers -- answer list used to check against user input for correct response
        num_of_tries -- the number of attempts a user gets to be correct
    Returns:
        user_input -- the input that the user provided, if corect
        max_attempts -- the 'fail' string if the user fails the quiz
    """
    tries = 0
    location = quiz_blanks.index(replacement_needed)
    while tries < num_of_tries:
        user_input = raw_input("Enter answer for " + replacement_needed + ": ")
        if user_input == quiz_answers[location]:
            return str(user_input)
            tries += num_of_tries
        else:
            print "Incorrect, try again."
            tries += 1
            print str(num_of_tries - tries) + " attempts left!"
    max_attempts = "You've reached the max attempts. Please try the quiz again."
    return max_attempts
        
    
start_quiz()
