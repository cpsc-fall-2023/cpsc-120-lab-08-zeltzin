#!/usr/bin/env python3
#
# Copyright 2021-2023 Michael Shafae
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html

# ex.
# .action/solution_check_p1.py  part-1 asgt

import io
import math
import sys
import os
import re
import pexpect
from assessment import csv_solution_check_make
from logger import setup_logger

import lab_config as cfg

def regex_it(s):
    combine_white_space_regex = re.compile(r"\s+")
    s = combine_white_space_regex.sub(" ", s).strip()
    s = s.replace(' ', '\\s+').replace('\n', '\\s+')
    return f'\\s*{s}\\s*'


def run_p1(binary):
    """Run part-1 command line madlib"""
    logger = setup_logger()
    status = []
    error_values = (
        [], # 0 arguments, too few
        ['ham'], # 1 arguments, too few
        ['ham', 'rye'], # 2 arguments, too few
        ['ham', 'rye', 'tomato', 'lettuce'], # 4 arguments, too many
    )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p1_error(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    
    values = (
                ['ham', 'rye', 'mayo'],
                ['tuna', 'wheat', 'mustard'],
                ['roast beef', 'kaiser roll', 'horse radish and mayo'],
                ['salami', 'white', 'cheddar'],
            )
    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p1(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p1_error(binary, values):
    """The actual test with the expected input and output"""
    logger = setup_logger()
    status = False
    proc = pexpect.spawn(binary, timeout=1, args=values)

    try:
        proc.expect(r'(?i)\s*error:.+')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logger.error('Expected: "error: you must supply three arguments"')
        logger.error('Could not find expected output.')
        logger.debug("%s", str(exception))
        logger.debug(str(proc))
        return status

    proc.close()

    if proc.exitstatus == 0:
        logger.error('Expected: non-zero exit code.')
        logger.error('Program returned zero, but non-zero is required')
        return status

    status = True
    return status

# based on lab 03, but modified to give input as command line arguments
def _run_p1(binary, values):
    """The actual test with the expected input and output"""
    logger = setup_logger()
    status = False
    values = list(values)
    proc = pexpect.spawn(binary, timeout=1, args=values)

    try:
        regex = r'(?i)\s*Your\s+order.?\s+A\s+{}\s+sandwich\s+on\s+{}\s+with\s+{}.?\s*'.format(*values)
        proc.expect(regex)
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logger.error('Expected:"Your order:\nA {} sandwich on {} with {}."'.format(*values))
        logger.error('Could not find expected output.')
        logger.debug("%s", str(exception))
        logger.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()

    if proc.exitstatus != 0:
        logger.error('Expected: zero exit code.')
        logger.error('Program returned non-zero, but zero is required')
        return status

    status = True
    return status

def run_p2(binary):
    """Run part-2 average"""
    logger = setup_logger()
    status = []
    error_values = (
        [], # 0 arguments, too few
    )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p2_error(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)

    values = (
                [1, 2, 3, 2],
                [10, 20, 15],
                [5, 5, 5],
                [1.2, 1.8, 1.5],
                [-3, 5, 1],
                [-2, -4, -3],
                [2, 3, 2.5],
                [7, 1, 2, 3.333],
                [6, 6],
                [0, 0],
                [0, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5.5],
            )

    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p2(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p2_error(binary, values):
    """The actual test with the expected input and output"""
    logger = setup_logger()
    status = False
    proc = pexpect.spawn(binary, timeout=1, args=values)

    try:
        proc.expect(r'(?i)\s*error:.+')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logger.error('Expected: "error: you must supply at least one number"')
        logger.error('Could not find expected output.')
        logger.debug("%s", str(exception))
        logger.debug(str(proc))
        return status

    proc.close()

    if proc.exitstatus == 0:
        logger.error('Expected: non-zero exit code.')
        logger.error('Program returned zero, but non-zero is required')
        return status

    status = True
    return status

def _run_p2(binary, values):
    """The actual test with the expected input and output"""
    import math
    logger = setup_logger()
    status = False
    expected = values[-1]
    proc = pexpect.spawn(binary, timeout=1, args=[str(val) for val in values[:-1]])
    values = list(map(str, values))

    try:
        # Match and extract the floating point number
        match_index = proc.expect(r'(?i)\s*average\s*=\s*([-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?)\s*')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logger.error('Expected: "average = %f"', expected)
        logger.error('Could not find expected output.')
        logger.debug("%s", str(exception))
        logger.debug(str(proc))
        return status

    token = proc.match.group(1).decode("utf-8") 
    actual = float(token)
    # 1% tolerance
    if not math.isclose(expected, actual, rel_tol=.01): 
        logger.error('actual numeric output is %f, which does not equal %f', actual, expected)
        return status

    proc.close()

    if proc.exitstatus != 0:
        logger.error('Expected: zero exit code.')
        logger.error('Program returned non-zero, but zero is required')
        return status

    status = True
    return status

if __name__ == '__main__':
    cwd = os.getcwd()
    repo_name = os.path.basename(cwd)
    td = sys.argv[1]
    # print(td)
    if sys.argv[1] == 'part-1':
        part_config = cfg.lab['parts'][0]
    elif sys.argv[1] == 'part-2':
        part_config = cfg.lab['parts'][1]
    else:
        print(f'Error: {sys.argv[0]} no match.')
        sys.exit(1)

    _program_name = part_config['target']
    _files = part_config['src'].split() + part_config['header'].split()
    _do_format_check = part_config['do_format_check']
    _do_lint_check = part_config['do_lint_check']
    _do_unit_tests = part_config['do_unit_tests']
    _tidy_options = part_config['tidy_opts']
    _skip_compile_cmd = part_config['skip_compile_cmd']
    # There needs to be some magic here to figure out which due date to use.
    _lab_due_date = cfg.lab['mon_duedate'].isoformat()
    _run_func = locals()[part_config['test_main']]

    # Execute the solution check
    csv_solution_check_make(
        csv_key=repo_name,
        target_directory=td,
        program_name=_program_name,
        run=_run_func,
        files=_files,
        do_format_check=_do_format_check,
        do_lint_check=_do_lint_check,
        do_unit_tests=_do_unit_tests,
        tidy_options=_tidy_options,
        skip_compile_cmd=_skip_compile_cmd,
        lab_due_date=_lab_due_date,
    )
