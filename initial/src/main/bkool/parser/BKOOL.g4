// Student ID: 1811915

grammar BKOOL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options{
	language=Python3;
}

// ---- PARSER -----------------------------------

// --- [1] Structure -----------------------------
program         : classDeclList EOF;
//program         : classDecl+ EOF;
classDeclList   : classDecl classDeclList
                | classDecl;
classDecl       : CLASS ID EXTENDS ID LP memberList RP
                | CLASS ID LP memberList RP
                | CLASS ID EXTENDS ID LP RP
                | CLASS ID LP RP;

memberList      : member memberList
                | member;
member          : attrKeyword attrType attrList SEMI
                | attrType attrList SEMI
                | STATIC returnType method SEMI
                | returnType method SEMI;

// attribute declare: <keyword> <type> (<ID> <ASSIGN> <exp>, <ID> <ASSIGN> <exp>, <ID>,...)
attrKeyword     : STATIC FINAL | FINAL STATIC | STATIC | FINAL;
attrType        : INT | FLOAT | BOOLEAN | STRING;
attrList        : attribute COMMA attrList
                | attribute;
attribute       : ID INIT exp
                | ID;

returnType      : INT | FLOAT | BOOLEAN | STRING | VOID;
method          : ID LB paramList RB blockStmt
                | ID LB RB blockStmt;
paramList       : param SEMI paramList
                | param;
param           : attrType idList;
idList          : ID COMMA idList
                | ID;
/*
		Special instance method: constructor method
		has no return_type and no return statements in block

		constrMethod: ID LP (paramList | EMPTY) RP blockStatementWithoutReturn;
*/              
    
// --- [2] Expressions -------------------------
// exp     : exp1 (LESS | GREATER | LEQ | GREQ) exp1
//         | exp1;
// exp1    : exp2 (EQ | NEQ) exp2
//         | exp2;
// exp2    : exp2 (AND | OR) exp3
//         | exp3;
// exp3    : exp3 (ADD | SUB) exp4
//         | exp4;
// exp4    : exp4 (MUL | DIV | DIVF | MOD) exp5
//         | exp5;
// exp5    : exp5 CONCAT exp6
//         | exp6;
// exp6    : NOT exp6
//         | exp7;
// exp7    : (ADD | SUB) exp7
//         | exp8;
// exp8: exp9;
// exp9: exp10;
// // exp8    : index_op
// //         | exp9;
// // exp9    : memAccess
// //         | exp10;
// exp10   : LB exp RB
//         | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | ARRAYLIT
//         | ID;

exp         : LB exp RB | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | ARRAYLIT | ID       // highest priority

            | exp DOT ID                // instance_attr_access
            | ID DOT ID                 // static_attr_access
            | exp DOT ID LB argList RB  // instance_method_invoke
            | exp DOT ID LB RB          // instance_method_invoke
            | ID DOT ID LB argList RB   // static_method_invoke
            | ID DOT ID LB RB           // static_method_invoke

            | exp LQ exp RQ             // index_op

            | (ADD | SUB) exp
            | NOT exp
            | exp CONCAT exp
            | exp (MUL | DIV | DIVF | MOD) exp
            | exp (ADD | SUB) exp
            | exp (AND | OR) exp
            | exp (EQ | NEQ) exp
            | exp (LESS | GREATER | LEQ | GREQ) exp;

// index_op    : exp LQ exp RQ;

memAccess               : exp DOT ID                // instance_attr_access
                        | ID DOT ID                 // static_attr_access
                        | exp DOT ID LB argList RB  // instance_method_invoke
                        | exp DOT ID LB RB          // instance_method_invoke
                        | ID DOT ID LB argList RB   // static_method_invoke
                        | ID DOT ID LB RB;          // static_method_invoke
// instance_attr_access    : exp DOT ID;
// static_attr_access      : ID DOT ID;
// instance_method_invoke  : exp DOT ID LB argList RB
//                         | exp DOT ID LB RB;
// static_method_invoke    : ID DOT ID LB argList RB
//                         | ID DOT ID LB RB;
argList                 : exp COMMA argList
                        | exp;

        

// --- [3] Statements ------------------------

stmtList    : stmt stmtList
            | stmt;
stmt        : blockStmt                 // each stmt's subrule has its own SEMI or other ending tokens
            | assignStmt
            | ifStmt
            | forStmt
            | breakStmt
            | continueStmt
            | returnStmt
            | methodInvokeStmt;


blockStmt   : LP blockBody RP;
blockBody   : declList stmtList
            | declList
            | stmtList;
declList    : decl declList
            | decl;
decl        : FINAL? attrType attrList SEMI;

assignStmt  : lhs ASSIGN exp SEMI;
lhs         : ID
            | exp DOT ID                // instance_attr_access
            | ID DOT ID                 // static_attr_access
            | exp LQ exp RQ;

ifStmt      : IF exp THEN stmt ELSE stmt
            | IF exp THEN stmt;

forStmt     : scalarVar ASSIGN exp (TO | DOWNTO) exp DO stmt;
scalarVar   : ID
            | exp DOT ID | ID DOT ID
            | exp LQ exp RQ;

breakStmt   : BREAK SEMI;
continueStmt: CONTINUE SEMI;

returnStmt  : RETURN exp SEMI;

methodInvokeStmt: CLASS CLASS;


/*

--- Program Structure -----------------------
	NOTE: < > = optional

	1/ Class declaration
		classDecl: CLASS ID <EXTENDS ID> LB memberList RB
		
		memberList: member memberList
				  | member
				  | EMPTY;
		member: (STATIC FINAL | FINAL STATIC | STATIC | FINAL | EMPTY) attribute SEMI
			  | (STATIC | EMPTY) method SEMI;
		attribute: type attrNameList;
		type: INT | FLOAT | BOOL | STRING;
		attrNameList: attrName COMMA attrNameList
					| attrName;
		attrName: ID EQUAL exp
				| ID;
		method: return_type ID LP (paramList | EMPTY) RP blockStatement;
		paramList: param SEMI paramList
				 | param;
		return_type (section 4)
		blockStatement (section 6.1)
		
		// Special instance method: constructor method
		// has no return_type and no return statements in block
		constrMethod: ID LP (paramList | EMPTY) RP blockStatementWithoutReturn;
		
--- Lexical Structure -----------------------

--- Type ------------------------------------
	4.1/ Primitive
		int:
			may be positive/negative
			operators: + - * / < <= > >= == != \ %
		float:
			operators: + - * / < <= > >=
		bool:
			true/false
			if statements work with bool exp
			operators: == != ! && ||
		string:
			operator: ^
		void:
			only used as a return type of a method when it has nothing to return
			NOT allowed for variable, const, param declaration
		array:
			ARRAY: type LQ INTLIT RQ
			# INTLIT = size (probably no negatives?)
		class:
			OBJ_CREATE: NEW ID LB RB;
			# also check 5.7

--- Expression -------------------------------
	# TODO!!!!!!!!!!!!!
	# For next assignments!!!!!
	
	2 types: unary, binary
	
	5.1/ Arithmetic:
		Operators: 
			+ - (prefix unary)
			+ - * / \ % (infix binary)
		# for type assignment?
	
	5.2/ Bool:
		Operators:
			&& || !
	
	5.3/ Relational:
		Operators: == != > < >= <=
		
	5.4/ String:
		Operator: ^
		Returns a new string that appends 2nd string to 1st string
		
	5.5/ Index:
		index_op: exp LQ exp RQ
	
	5.6/ Member access:
		instance_attr_access: exp DOT ID
		(exp returns an object of a class, ID is an attribute of the class)
		
		static_attr_access: ID DOT ID
		(ID1 is class name, ID2 is a static attribute)
		
		instance_method_invoke: exp DOT ID LB (argList | EMPTY) RB;
		argList: exp COMMA argList
			   | exp;
			returns same type as invoked method
			
		static_method_invoke: ID DOT ID LB (argList | EMPTY) RB;
			...
			
	5.7/ Object creation:
		obj_create: NEW ID LB (argList | EMPTY) RB;
		
	5.8/ This:
		# this = current obj of the enclosing class
		# same type as enclosing class' type
	
	5.9/ Operator Precedence/Associativity:
		Order of precedence from high to low:
			
			new (R)
			. (L)
			[ ]
			+ - (unary) (R)
			! (R)
			^ (L)
			* / \ % (L)
			+ - (binary) (L)
			&& || (L)
			== != (none)
			< > <= >= (none)
			
	5.10/ Type coercion:
		Mixed-mode expressions: operands have different types
		+ - * / < <= > >=
		# TODO!!!!!!!!!!!!!!
		# for later assignments!!!!
		
	5.11/ Evaluation order:
		Binary operator: lhs evaluated first
		Method invocation: parameters evaluated L->R
		
		All operands evaluated first before operation
		EXCEPTION: && || (short circuiting)
		for code generation assignment!!!!
		
			
--- Statement -----------------------------------
	Doesn't return anything
	
	6.1/ Block statement
		LP blockBody RP
		
		blockBody: declList? stmtList?;
		declList: decl declList
				| decl;
		decl: FINAL? attribute SEMI;
		
			# reminder
			agwetevtw5t2!!!!!!!!!
			attribute: attrNameList;
			type: INT | FLOAT | BOOL | STRING;
			attrNameList: attrName COMMA attrNameList
						| attrName;
			attrName: ID EQUAL exp
					| ID;
					
	6.2/ Assign statement
		Assigns value to local variable/mutable attribute/ele of array
		
		assignStmt: assign_lhs COLON EQUAL exp SEMI;
		# assign_lhs = local variable/mutable attr/ele of array
		# TODO!!!!!!!!!!!!!!!!
		
	6.3/ If statement
		ifStmt: IF exp THEN stmt (ELSE stmt)?;
		# exp evaluates to bool value
		
	6.4/ For statement
		forStmt: FOR scalar_var COLON EQUAL exp1 (TO | DOWNTO) exp2 DO stmt
		
		First:
			exp1 is evaluated, then assigned to scalar_var
			evaluates exp2
			if TO:
				if exp1 (= scalar_var) <= exp2, then stmt
				scalar_var++
			if DOWNTO:
				if exp1 (= scalar_var) >= exp2, then stmt
				scalar_var--
				
	6.5/ Break
		breakStmt: BREAK SEMI;
		
		# only in loops
		# TODO!!!!!!!!!!!!!!!!!
		# for Semantic Analysis phase!!!!
		
	6.6/ Continue
		continueStmt: CONTINUE SEMI;
		
		# only in loops
		# TODO!!!!!!!!!!!!!!!!!
		# for Semantic Analysis phase!!!!
		
	6.7/ Return statement
		returnStmt: RETURN exp SEMI;
		
		# transfer control to caller of the method that invokes it
	
	6.8/ Method invocation statement
		# check 5.6
		
		methodInvokeStmt: (instance_method_invoke | static_method_invoke) SEMI;
 
 
*/


// ---- LEXER ------------------------------------

// ------ Base fragments -------
    // fragment EMPTY: '';
    fragment DIGIT: [0-9];
    fragment CHAR: [A-Za-z];

// ------ Whitespaces -------
    WS: [ \t\f\r\n] -> skip;
	
// ------ Comments -------
    BLOCK_CMT: '/*' .*? '*/' -> skip;
    LINE_CMT: '#' .*? ('\n' | EOF) -> skip;

// ------ Keywords ------
    BOOLEAN: 'boolean';
    BREAK: 'break';
    CLASS: 'class';
    CONTINUE: 'continue';
    DO: 'do';
    ELSE: 'else';
    EXTENDS: 'extends';
    FLOAT: 'float';
    IF: 'if';
    INT: 'int';
    NEW: 'new';
    STRING: 'string';
    THEN: 'then';
    FOR: 'for';
    RETURN: 'return';
    TRUE: 'true';
    FALSE: 'false';
    VOID: 'void';
    NIL: 'nil';
    THIS: 'this';
    FINAL: 'final';
    STATIC: 'static';
    TO: 'to';
    DOWNTO: 'downto';

// ------ Identifier ------
    ID: (CHAR | UNDERSCORE) (CHAR | DIGIT | UNDERSCORE)*;
    fragment UNDERSCORE: '_';

// ------ Operators ------
    ADD: '+';
    SUB: '-';
    MUL: '*';
    DIV: '\'';
    DIVF: '/';
    MOD: '%';
    NEQ: '!=';
    EQ: '==';
    LESS: '<';
    GREATER: '>';
    LEQ: '<=';
    GREQ: '>=';
    OR: '||';
    AND: '&&';
    NOT: '!';
    CONCAT: '^';
    // object creation: 'new'

    ASSIGN: ':=';
    INIT: '=';
	
// ------ Separators ------
    LP: '{';
	RP: '}';
	LB: '(';
	RB: ')';
	LQ: '[';
	RQ: ']';
	SEMI: ';';
	COLON: ':';
	DOT: '.';
	COMMA: ',';
	
// ------ Literal ------
// Source representation of an int/float/bool/string value
		
	// Int literal
	INTLIT: DIGIT+;

	// Float literal
	FLOATLIT: DIGIT+ FLOAT_END;
	fragment FLOAT_END: DECPART EXPPART
					  | DECPART
					  | EXPPART;
					  
	fragment DECPART: DOT DIGIT*;
	fragment EXPPART: [Ee] SIGN? DIGIT+;
	fragment SIGN: [+-];
			
	// Bool literal
	BOOLLIT: (TRUE | FALSE);
			
	// String literal
    fragment ESCAPE: [\b\f\r\t\\];
    fragment ILLEGAL_ESC:   '\\' ~[bfrt"\\];
    fragment CHARS: (~["\n] | ESCAPE | '\\"');      // in a string, \ can only appear as \\


    STRINGLIT: '"' CHARS* '"'{
        self.text = (str(self.text))[1:-1]
    };
	/*	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			fragment ESC_SEQ:
			STRINGLIT:
    */
			
	// Array literal
	ARRAYLIT: LP LITERAL LITLIST RP
            | LP LITERAL RP;
	LITLIST : COMMA LITERAL LITLIST
            | COMMA LITERAL;
			
	fragment LITERAL: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;



// ------ Errors ------
// ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;

ERROR_CHAR: .{
    raise ErrorToken(self.text)
};
UNCLOSE_STRING: '"'CHARS*{
    raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"'CHARS* ILLEGAL_ESC{
    raise IllegalEscape(self.text[1:])
};