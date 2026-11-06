package org.example.basics

object ScopeFunctions {

    //
    // Scope functions provide a way to execute a code block to (in theory) increase readability.
    //

    fun letExample(pair: Pair<Int, String>?) {
        if (pair != null) {
            val (int, string) = pair
            println("$int $string")
        }

        // let transforms the value into another type of value
        val outputString = pair?.let { (int, string) -> "$int $string" }
        println(outputString)

        // Unit is also "another type of value"
        pair?.let { (int, string) -> println("$int $string") }
    }

    fun otherExamples() {
        // also executes a side effect, but returns the original value
        val alsoVal = 1.also { i -> println(i) } // alsoVal == 1

        // run pretends to be an instance function (access to `this`), maps to new value
        val runVal = 1.run { this + 1 } // runVal == 2

        // apply pretends to be an instance function (access to `this`), performs side effects, returns modified val
        val applyVal = mutableListOf<Int>().apply {
            this.add(1)
            add(2) // implicit access to `this` fns
            add(3)
        } // applyVal == mutableListOf(1, 2, 3)

        // with pretends to be an instance function (access to `this`), performs side effects, maps to new value
        val withVal = with(mutableListOf<Int>()) {
            add(4)
            add(5)
            add(6)
            this.toList()
        } // withVal = listOf(4, 5, 6)

    }
}