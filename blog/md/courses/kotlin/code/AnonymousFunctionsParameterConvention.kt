package org.example.basics

object AnonymousFunctionsParameterConvention {

    fun transform(list: List<Int>, fn: (Int) -> String) : List<String> {
        val result = mutableListOf<String>()
        for (item in list) {
            result.add(fn(item))
        }
        return result
    }

    fun useFn() {
        val intList = listOf(1, 2, 3)

        val stringList1 = transform(intList, { it.toString() })

        // equivalent
        val stringList2 = transform(intList) { it.toString() }

    }

}