# Python switching methods

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]


def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9)    # 9 is default if x not found



# from http://code.activestate.com/recipes/410692/

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.
v = 'ten'
for case in switch(v):
    if case('one'):
        print 1
        break
    if case('two'):
        print 2
        break
    if case('ten'):
        print 10
        break
    if case('eleven'):
        print 11
        break
    if case(): # default, could also just omit condition or 'if True'
        print "something else!"
        # No need to break here, it'll stop anyway

# break is used here to look as much like the real thing as possible, but
# elif is generally just as good and more concise.

# Empty suites are considered syntax errors, so intentional fall-throughs
# should contain 'pass'
c = 'z'
for case in switch(c):
    if case('a'): pass # only necessary if the rest of the suite is empty
    if case('b'): pass
    # ...
    if case('y'): pass
    if case('z'):
        print "c is lowercase!"
        break
    if case('A'): pass
    # ...
    if case('Z'):
        print "c is uppercase!"
        break
    if case(): # default
        print "I dunno what c was!"

# As suggested by Pierre Quentel, you can even expand upon the
# functionality of the classic 'case' statement by matching multiple
# cases in a single shot. This greatly benefits operations such as the
# uppercase/lowercase example above:
import string
c = 'A'
for case in switch(c):
    if case(*string.lowercase): # note the * for unpacking as arguments
        print "c is lowercase!"
        break
    if case(*string.uppercase):
        print "c is uppercase!"
        break
    if case('!', '?', '.'): # normal argument passing style also applies
        print "c is a sentence terminator!"
        break
    if case(): # default
        print "I dunno what c was!"

# Since Pierre's suggestion is backward-compatible with the original recipe,
# I have made the necessary modification to allow for the above usage.




# from http://code.activestate.com/recipes/181064/

#! /usr/local/bin/python

# /////////////////////////////////////////////////////////////////////////
# /**
# * Title: rochambeau.py
# *
# * Description: Rock, Scissors, Paper Game. 
# *              Shows a clean way of implementing a 'switch'
# *              statement in Python via a dictionary container. 
# *              The dictionary is made up of known 'named states' that
# *              are tested in sequence for their current 'state'.
# *
# * Copyright: Copyright (c) 2003
# *            This file is distributed as EXAMPLE SOURCE CODE ONLY!
# *            The following code is considered 'Freeware' and can be 
# *            freely copied/reused/distributed as needed. 
# *
# * Company: None
# * @author: Alan Haffner
# * @version 1.0
# */
# 
# /////////////////////////////////////////////////////////////////////////
# Date: 02/16/03


import os, sys
import string, random
import types

def cli():

   c = '?'
   while c not in 'rps':

      try:
         print
         # tailing index '[0]' picks only first char from input
         c = raw_input('\tPlease enter (r)ock, (p)aper or (s)cissors to play... ')[0]
      except IndexError:
         # bad input, so like get another...
         pass

      c = c.lower()

      #   x, q...   --> quit
      if c in ('x', 'q' ):
         raise 'USER_QUIT_ERROR'

   return c

if __name__=='__main__':

   errorCode = 0

   stateList = ['r', 'p', 's']

   validStates = { 'User Wins'      : (('p','r'), ('r','s'), ('s','p')),
                   'No One Wins'    : (('p','p'), ('r','r'), ('s','s')),
                   'Computer Wins'  : (('r','p'), ('s','r'), ('p','s')),
   }

   try:
      while 1:
         testTuple     = (None, None)
         userInput     =        None
         computerInput =       '?'

         userInput     = cli()
         computerInput = ( stateList[random.randint(0,2)] )
   
         testTuple = (userInput, computerInput)

         for select in validStates:
            if testTuple in validStates[select]:
               print
               print "You chose:         ", userInput
               print "The computer chose:", computerInput
               print " ****", select, " ****" 
               print

   # Note: By convention, all local exception 'constants' end 
   # in '_ERROR' regaurdless of their intended use. 
   except KeyboardInterrupt:
      print '\n' * 3
      print '[interrupted by user]'
      print '\n' * 3
   except 'USER_QUIT_ERROR':
      print '\n' * 3
      print '[interrupted by user]'
      print '\n' * 3
   except:
      # unexpected error
      print '\n' * 3
      traceback.print_exc()
      print '\n' * 3

      errorCode = 2

   sys.exit(errorCode)

