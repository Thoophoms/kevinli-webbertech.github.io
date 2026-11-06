package org.example.basics

object TypeInference {

    //
    // Local variable types will be inferred if possible.
    //

    fun examples() {
        val int = 1
        val long_ = 2L
        val double_ = 3.0
        val float_ = 4.0f

        val intList = listOf(1, 2, 3, 4, 5)
        val stringList = listOf("a", "b", "c")
        val emptyIntList = listOf<Int>()
        val emptyIntList2 : List<Int> = listOf()
    }

}