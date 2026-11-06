package org.example.basics

object Nulls {

    //
    // nulls are explicit
    //

    fun printSize(list: List<String>) {
        println(list.size)
    }

    fun printSize2(list: List<String>?) {
        if (list != null)
            println(list.size)
        else
            println(null) // "null"
    }

    //
    // null-safe operators
    //

    fun printSize3(list: List<String>?) {
        val size = list?.size
        println(list?.size)
    }

    fun printSize4(list: List<String>?) {
        val size = list?.size ?: 0
        println(size)
    }

}