male(john).
male(peter).
male(mark).
male(david).
male(james).

female(mary).
female(susan).
female(linda).
female(anne).
female(sarah).

parent(john, peter).
parent(mary, peter).

parent(john, linda).
parent(mary, linda).

parent(peter, mark).
parent(susan, mark).

parent(peter, anne).
parent(susan, anne).

parent(linda, david).
parent(james, david).

parent(linda, sarah).
parent(james, sarah).


% RULES
father(X,Y) :-
    male(X),
    parent(X,Y).
mother(X,Y) :-
    female(X),
    parent(X,Y).
grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).
grandchild(X,Y) :-
    grandparent(Y,X).
sibling(X,Y) :-
    parent(Z,X),
    parent(Z,Y),
    X \= Y.
cousin(X,Y) :-
    parent(A,X),
    parent(B,Y),
    sibling(A,B).
uncle(X,Y) :-
    male(X),
    sibling(X,Z),
    parent(Z,Y).
aunt(X,Y) :-
    female(X),
    sibling(X,Z),
    parent(Z,Y).


% TEST QUERIES AND EXPECTED RESULTS

% Query: to find the father of Mark
% ?- father(X, mark).
% Expected Result:
% X = peter.

% Query: to find the mother of Anne
% ?- mother(X, anne).
% Expected Result:
% X = susan.

% Query: to find the grandparents of Mark
% ?- grandparent(X, mark).
% Expected Result:
% X = john ;
% X = mary.

% Query: to find the father of David
% ?- father(X, david).
% Expected Result:
% X = james.


% Query: to find the mother of Mark
% ?- mother(X, mark).
% Expected Result:
% X = susan.

% Query: to find the children of Peter
% ?- parent(peter, X).
% Expected Result:
% X = mark ;
% X = anne.
% Query: to find the grandchildren of John
% ?- grandchild(X, john).
% Expected Result:
% X = mark ;
% X = anne ;
% X = david ;
% X = sarah.
