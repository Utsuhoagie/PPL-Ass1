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
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

// ---- PARSER -----------------------------------

program  : EOF ;



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

// ------ Identifier ------
    ID: (CHAR | UNDERSCORE) (CHAR | DIGIT | UNDERSCORE)*;
    fragment UNDERSCORE: '_';
	
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
    fragment DOUBLEQUOTES: '\"';
    fragment CHARS: (~["\n] | ESCAPE);
    STRINGLIT: '"' CHARS* '"';
	/*	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			fragment ESC_SEQ:
			STRINGLIT:
    */
			
	// Array literal
	ARRAYLIT: LP LITERAL LITLIST? RP;
	LITLIST: COMMA LITERAL LITLIST;
			
	fragment LITERAL: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;



// ------ Errors ------
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;