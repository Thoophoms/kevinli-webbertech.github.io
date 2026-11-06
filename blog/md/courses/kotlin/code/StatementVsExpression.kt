package org.example.basics

import kotlin.math.roundToInt

object StatementVsExpression {

    // TODO less contrived example

    fun statementExample(list: List<Int>) : Boolean {
        var found = false
        if (list.average().roundToInt() == 7) {
            found = true // executes side effect
        }
        return found
    }

    fun expressionExample(list: List<Int>) : Boolean {
        val found = if (list.average().roundToInt() == 7) {
            true // returns a value
        } else {
            false // all branches must return a value
        }
        return found
    }

    fun functionExpression(list: List<Int>) : Boolean = // notice equal sign instead of curly braces
        if (list.average().roundToInt() == 7) true else false


}