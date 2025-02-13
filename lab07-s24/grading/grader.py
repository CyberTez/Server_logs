"""
We define a comboSuite to combine multiple test files into a single test file
to execute.

Students - DO NOT MODIFY THIS FILE!

"""

import os
import sys
import unittest

def list_py_files(subfolder):
    py_files = []
    for root, dirs, files in os.walk(subfolder):
        for file in files:
            if file.endswith('.py') and "__init__" not in file:
                py_files.append(os.path.join(root, file))
    return py_files

def score_style(files):
    """
    Calculate overall style points from list of files

    @param: files - list of source files to check
    @return: score 0 to 100
    """
    print(f"\nRunning pylint checker ...", flush=True)
    try:
        from grading.lint_test import lint_test
    except Exception as exc:
        print(exc)
        print(" cannot run lint test!")
        return 0

    total_style = 0

    for file in files:
        print(f"\n  Running pylint for {file} ...")
        try:
            passed, style = lint_test(file)
        except Exception as exc:
            print(exc, flush=True)
            score = 0

        total_style += style
        print(20*"-")

    # Convert to percentage points
    if len(files) > 0:
        style = total_style*(10./len(files)) # total style in percentage
        if style < 0.0:
            style = 0.0
    else:
        style = 0.0

    print(30*"=")
    print(f"  Total style percentage = {style:6.2f}", flush=True)
    return style

def grade_repo(args):
    """
    Define the project grader for specific files
    """

    """
    Customize this list of tests and files for each week
    """

    print("Grading repo ...", flush=True)
    try:

        files = list_py_files('src')
        print('Files:', files)
        style_score = score_style(files)
    except Exception as exc:
        print(exc, flush=True)
        style_score = 0.0


    hw_score = 0.0  # No separate HW grade for lab
    final_grade = 0.20*style_score

    print(f"#Style points = {final_grade:6.1f} of 20", flush=True)

    return final_grade

if __name__ == "__main__":

    # Usage:
    # PYTHONPATH=. python3 $UNITTEST $GITLAB_USER_LOGIN $CI_PROJECT_NAME $CI_COMMIT_SHORT_SHA $CI_COMMIT_TIMESTAMP $CI_PIPELINE_CREATED_AT $CI_COMMIT_AUTHOR
    # At least user is required!
    #print(sys.argv)
    if grade_repo(sys.argv[1:]) < 18: # For lab style points
        # Give an X on Gitlab CI page
        sys.exit(-1)  # Some grading error to fix
