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

//cum: IF cum | ;

program         : classDeclList EOF;
classDeclList   : classDecl classDeclList
                | classDecl;
classDecl       : CLASS ID EXTENDS ID LP (memberList | ) RP
                | CLASS ID LP (memberList | ) RP;
/*
                | CLASS ID EXTENDS ID LP RP
                | CLASS ID LP RP;
*/

memberList      : member memberList
                | member;
member          : (attrKeyword | ) attrType attrList SEMI
//                | attrType attrList SEMI
                | (STATIC | ) returnType method;
//                | returnType method;

attrKeyword     : STATIC FINAL | FINAL STATIC | STATIC | FINAL;
attrType        : INT | FLOAT | BOOLEAN | STRING | ID | arrayType;  // ID is for class names (e.g Shape s)
arrayType       : (INT | FLOAT | BOOLEAN | STRING) LQ INTLIT RQ;
attrList        : attribute COMMA attrList
                | attribute;
attribute       : ID INIT exp
                | ID;

returnType      : INT | FLOAT | BOOLEAN | STRING | VOID;
method          : ID LB (paramList | ) RB blockStmt;
//                | ID LB RB blockStmt;
paramList       : param SEMI paramList
                | param;
param           : attrType idList;
idList          : ID COMMA idList
                | ID;
    
// --- [2] Expressions -------------------------



exp         : LB exp RB | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | ARRAYLIT | THIS | ID    // highest priority
            | obj_create
            | exp DOT ID LB (argList | ) RB // instance_method_invoke
            | ID DOT ID LB (argList | )RB   // static_method_invoke
            | exp DOT ID                    // instance_attr_access
            | ID DOT ID                     // static_attr_access


            | exp LQ exp RQ                 // index_op

            | (ADD | SUB) exp
            | NOT exp
            | exp CONCAT exp
            | exp (MUL | DIV | DIVF | MOD) exp
            | exp (ADD | SUB) exp
            | exp (AND | OR) exp
            | exp (EQ | NEQ) exp
            | exp (LESS | GREATER | LEQ | GREQ) exp;

argList     : exp COMMA argList
            | exp;


obj_create  : NEW ID LB (argList | ) RB;
//            | NEW ID LB RB;

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


blockStmt   : LP (blockBody | ) RP;
            //| LP RP;
blockBody   : (declList | ) (stmtList | );
//            | declList
//            | stmtList;
declList    : decl declList
            | decl;
decl        : (FINAL | ) attrType attrList SEMI;
//            | attrType attrList SEMI;

assignStmt  : lhs ASSIGN exp SEMI;
lhs         : ID
            | exp DOT ID                // instance_attr_access
            | ID DOT ID                 // static_attr_access
            | exp LQ exp RQ;

ifStmt      : IF exp THEN stmt ELSE stmt
            | IF exp THEN stmt;

forStmt     : FOR scalarVar ASSIGN exp (TO | DOWNTO) exp DO stmt;
scalarVar   : ID                        // local variable
            | exp DOT ID | ID DOT ID    // instance/static attribute access
            | exp LQ exp RQ;            // index_op

breakStmt   : BREAK SEMI;
continueStmt: CONTINUE SEMI;

returnStmt  : RETURN exp SEMI
            | RETURN SEMI;

methodInvokeStmt: exp DOT ID LB (argList | ) RB SEMI    // instance_method_invoke
//                | exp DOT ID LB RB SEMI               // instance_method_invoke
                | ID DOT ID LB (argList | ) RB SEMI;    // static_method_invoke
//                | ID DOT ID LB RB SEMI;               // static_method_invoke

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
	BOOLLIT: TRUE | FALSE;
			
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
	fragment LITLIST : COMMA LITERAL LITLIST
                     | COMMA LITERAL;
			
	fragment LITERAL: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;

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