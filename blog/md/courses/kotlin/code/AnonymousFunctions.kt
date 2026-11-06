package org.example.basics

object AnonymousFunctions {

    fun regularFn(a: Int) {
        println(a)
    }

    val anonymousFn = { a: Int ->
        println(a)
    }
    // type: (Int) -> Unit

    fun regularFnReturn(a: Int) : String {
        return "$a"
    }

    val anonymousFunReturn = { a: Int ->
        "$a"
    }
    // type: (Int) -> String

    fun regularFn2(a: Int, b: String) {
        println(a)
        println(b)
    }

    val anonymousFn2 = { a: Int, b: String ->
        println(a)
        println(b)
    }
    // type: (Int, String) -> String

    val regularFnAsAnonymous = ::regularFn


    fun usageExampleLists() {
        val list = listOf(1, 2, 3, 4, 5)

        // filter
        val filteredListOldWay = mutableListOf<Int>()
        for (i in list.indices) {
            val item = list[i]
            if (i % 2 == 0) {
                filteredListOldWay.add(item)
            }
        }

        val filterList = list.filter { item -> item % 2 == 0 }

        // transform
        val transformedListOldWay = mutableListOf<String>()
        for (i in list.indices) {
            val item = list[i]
            val transformedItem = "$item"
            transformedListOldWay.add(transformedItem)
        }

        val transformedList = list.map { item -> "$item" }

        // split list
        val leftListOldWay = mutableListOf<Int>()
        val rightListOldWay = mutableListOf<Int>()
        for (i in list.indices) {
            val item = list[i]
            if (item % 2 == 0) {
                leftListOldWay.add(item)
            } else {
                rightListOldWay.add(item)
            }
        }

        val (leftList, rightList) = list.partition { item -> item % 2 == 0 }

        // lots more collection functions exist in kotlin
        // https://kotlinlang.org/docs/collection-operations.html#common-operations
    }

    fun usageExampleIt() {
        val list = listOf(1, 2, 3, 4, 5)

        val filteredList1 = list.filter { item -> item % 2 == 0 }

        val filteredList2 = list.filter { it % 2 == 0 }


        val transformedList1 = list.map { item -> "$item" }

        val transformedList2 = list.map { "$it" }


        val (leftList1, rightList1) = list.partition { item -> item % 2 == 0 }

        val (leftList2, rightList2) = list.partition { it % 2 == 0 }
    }

}