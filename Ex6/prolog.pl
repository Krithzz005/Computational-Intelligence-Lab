[23bcs074@mepcolinux ex6]$cat arith
start :-
    write('Choose type: arithmetic / set'), nl,
    read(Type),
    process(Type).

/* ---------- MAIN PROCESS ---------- */

process(arithmetic) :-
    write('Enter first number: '), nl,
    read(X),
    write('Enter second number: '), nl,
    read(Y),
    write('Choose operation: add / subtract / multiply / divide / modulus / power'), nl,
    read(Op),
    calculate(Op, X, Y, R),
    write('Result is: '), write(R), nl.

process(set) :-
    write('Enter first set (as list): '), nl,
    read(S1),
    write('Enter second set (as list): '), nl,
    read(S2),
    write('Choose operation: union / intersection / difference'), nl,
    read(Op),
    set_operation(Op, S1, S2, R),
    write('Result is: '), write(R), nl.

/* ---------- ARITHMETIC OPERATIONS ---------- */

calculate(add, X, Y, R) :- R is X + Y.
calculate(subtract, X, Y, R) :- R is X - Y.
calculate(multiply, X, Y, R) :- R is X * Y.
calculate(divide, X, Y, R) :- Y \= 0, R is X / Y.
calculate(modulus, X, Y, R) :- Y \= 0, R is X mod Y.
calculate(power, X, Y, R) :- R is X ** Y.

/* ---------- SET OPERATIONS (NO HELPER) ---------- */

set_operation(union, S1, S2, R) :-
    union(S1, S2, R).

set_operation(intersection, S1, S2, R) :-
    intersection(S1, S2, R).

set_operation(difference, S1, S2, R) :-
    subtract(S1, S2, R).
[23bcs074@mepcolinux ex6]$cat pizza
:- dynamic pizza/3.

start :-
    menu.

menu :-
    nl,
    write('--- Pizza Hut Ordering System ---'), nl,
    write('1. Add Pizza'), nl,
    write('2. Order Pizza'), nl,
    write('3. Display Menu'), nl,
    write('4. Exit'), nl,
    write('Enter your choice: '),
    read(Choice),
    process(Choice).

process(1) :- add_pizza, menu.
process(2) :- order_pizza, menu.
process(3) :- display_menu, menu.
process(4) :- write('Thank you! Visit again.'), nl.
process(_) :- write('Invalid choice'), nl, menu.

/* ---------- ADD PIZZA ---------- */

add_pizza :-
    write('Enter pizza name: '), nl,
    read(Name),
    write('Enter price: '), nl,
    read(Price),
    write('Enter available quantity: '), nl,
    read(Qty),
    assertz(pizza(Name, Price, Qty)),
    write('Pizza added successfully!'), nl.

/* ---------- DISPLAY MENU ---------- */

display_menu :-
    write('Available Pizzas:'), nl,
    forall(pizza(Name, Price, Qty),
        (write(Name), write(' - Rs.'), write(Price),
         write(' - Qty: '), write(Qty), nl)
    ).

/* ---------- ORDER SECTION ---------- */

order_pizza :-
    write('Enter number of pizzas to order: '), nl,
    read(N),
    take_orders(N, Total),
    write('Total Bill = Rs.'), write(Total), nl.

/* ---------- ORDER PROCESS ---------- */

take_orders(0, 0).

take_orders(N, Total) :-
    N > 0,
    write('Enter pizza name: '), nl,
    read(Name),
    write('Enter quantity: '), nl,
    read(Qty),

    ( pizza(Name, Price, AvailableQty) ->
        ( Qty =< AvailableQty ->
            Subtotal is Price * Qty,
            write('Subtotal = Rs.'), write(Subtotal), nl,

            NewQty is AvailableQty - Qty,
            retract(pizza(Name, Price, AvailableQty)),
            assertz(pizza(Name, Price, NewQty)),

            N1 is N - 1,
            take_orders(N1, RestTotal),
            Total is Subtotal + RestTotal
        ;
            write('Not enough stock available!'), nl,
            take_orders(N, Total)
        )
    ;
        write('Pizza not found!'), nl,
        take_orders(N, Total)
    ).
[23bcs074@mepcolinux ex6]$cat fam
% ----------- GENDER -----------

female(sethu_lakshmi_bayi).
female(sethu_parvathi_bayi).
female(gowri_parvathi_bayi).
female(gowri_lakshmi_bayi).
female(keerthana_bayi).

male(sree_moolam_thirunal).
male(chithira_thirunal).
male(uthradom_thirunal).
male(moolam_thirunal).
male(aditya_varma).
male(arjun_varma).

% ----------- PARENTS (5 GENERATIONS) -----------

% LEVEL 1 → LEVEL 2
parent(sethu_lakshmi_bayi, sree_moolam_thirunal).
parent(sethu_parvathi_bayi, sree_moolam_thirunal).

% LEVEL 2 → LEVEL 3
parent(sree_moolam_thirunal, chithira_thirunal).
parent(sree_moolam_thirunal, uthradom_thirunal).

% LEVEL 3 → LEVEL 4
parent(chithira_thirunal, moolam_thirunal).
parent(gowri_parvathi_bayi, moolam_thirunal).

% LEVEL 4 → LEVEL 5
parent(moolam_thirunal, aditya_varma).
parent(gowri_lakshmi_bayi, aditya_varma).

parent(moolam_thirunal, arjun_varma).
parent(gowri_lakshmi_bayi, arjun_varma).

% EXTRA (extend realism)
parent(aditya_varma, keerthana_bayi).

% ----------- RULES -----------

father(X,Y) :- parent(X,Y), male(X).
mother(X,Y) :- parent(X,Y), female(X).

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
descendant(X, Y) :- parent(Y, X).

descendant(X, Y) :- parent(Y, Z), descendant(X, Z).

grandfather(X,Y) :- grandparent(X,Y), male(X).
grandmother(X,Y) :- grandparent(X,Y), female(X).

sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.
brother(X,Y) :- sibling(X,Y), male(X).
sister(X,Y) :- sibling(X,Y), female(X).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).
[23bcs074@mepcolinux ex6]$cat op

14 ?- consult(['c:/Users/keerthi/OneDrive/Documents/Prolog/arith.pl']).
true.

14 ?- calculate(add,12,5,R).
R = 17.

15 ?- calculate(sub,12,5,R).
false.

16 ?- calculate(subtract,12,5,R).
R = 7.

17 ?- calculate(multiply,12,5,R).
R = 60.

18 ?- calculate(divide,12,5,R).
R = 2.4.

19 ?- calculate(divide,12,5,R).
R = 2.4.

19 ?- set_operation(union, [1,2], [2,3], R).
R = [1, 2, 3].

20 ?- set_operation(intersection, [1,2], [2,3], R).
R = [2].

21 ?- set_operation(difference, [1,2], [2,3], R).
R = [1].


3. Exit
Enter your choice: 2
|: .
Available Pizzas:
margherita - Rs.200 - Qty: 10
veg_supreme - Rs.300 - Qty: 8
farmhouse - Rs.350 - Qty: 6
peppy_paneer - Rs.280 - Qty: 7

--- Pizza Hut Ordering System ---
1. Order Pizza
2. Display Menu
3. Exit
Enter your choice: |: 1.
Enter number of pizzas to order:
|: 3.

--- Order Details ---
Enter pizza name:
|: margherita.
Enter quantity:
|: 2
|: .
Pizza: margherita
Quantity: 2
Price per item: Rs.200
Subtotal: Rs.400

Enter pizza name:
|: farmhouse.
Enter quantity:
|: 1
|: .
Pizza: farmhouse
Quantity: 1
Price per item: Rs.350
Subtotal: Rs.350

Enter pizza name:
|: peppy_paneer.
Enter quantity:
|: 2.
Pizza: peppy_paneer
Quantity: 2

26 ?- parent(moolam_thirunal, X).
X = aditya_varma .

27 ?- father(X, aditya_varma).
X = moolam_thirunal .

28 ?- sibling(aditya_varma, arjun_varma).
true .

29 ?- brother(X, aditya_varma).
X = arjun_varma .

30 ?- grandparent(X, keerthana_bayi).
X = moolam_thirunal .

31 ?- ancestor(sethu_lakshmi_bayi, arjun_varma).
true .
[23bcs074@mepcolinux ex6]$exit
exit
