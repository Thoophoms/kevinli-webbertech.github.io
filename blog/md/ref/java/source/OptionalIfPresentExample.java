package com.webbertech.java;

import java.util.Optional;

public class OptionalIfPresentExample {

	public OptionalIfPresentExample() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {

		Optional<String> gender = Optional.of("MALE");
		Optional<String> emptyGender = Optional.empty();

		if (gender.isPresent()) {
			System.out.println("Value available.");
		} else {
			System.out.println("Value not available.");
		}

		gender.ifPresent(g -> System.out.println("In gender Option, value available."));

		// condition failed, no output print
		emptyGender.ifPresent(g -> System.out.println("In emptyGender Option, value available."));

	}

}
