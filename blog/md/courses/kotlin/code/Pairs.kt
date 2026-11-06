package org.example.basics

object Pairs {

    //
    // Pairs are an alternative to creating custom classes for temporary values.
    //

    val pair = Pair(1, "two")
    // equivalent
    val pair2 = 1 to "two"

    fun getPair() : Pair<Int, String> {
        return 1 to "one"
    }

    fun usePair() {
        // basic usage
        val pair = getPair()
        println("first " + pair.first)
        println("second " + pair.second)

        // destructure
        val (int, str) = getPair()
        println("first " + int)
        println("second " + str)
    }

    //
    // Triples also exist, but there's no special syntax like `to`
    //

    val triple = Triple(1, "two", 3.0)

}