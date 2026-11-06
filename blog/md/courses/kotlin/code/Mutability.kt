package org.example.basics

object Mutability {
    fun valueMutability() {
        val immutableInt = 1
        // doesn't work
        //immutableInt = immutableInt + 1

        var mutableInt = 1
        mutableInt = 2
        mutableInt++
        mutableInt += 2
        mutableInt -= 1

        val immList = listOf("a", "b", "c")
        // doesn't exist
        //immList.add
        val mutList = mutableListOf("a", "b", "c")
        mutList.add("d")
        mutList.remove("a")
        // mutList == mutableListOf("b", "c", "d")
    }

}