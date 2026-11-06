package org.example.basics

object ValueShadowing {
    fun shadowExample(value: Int) {
        println(value) // uses parameter

        val value = value + 1
        println(value) // uses local val
    }
}