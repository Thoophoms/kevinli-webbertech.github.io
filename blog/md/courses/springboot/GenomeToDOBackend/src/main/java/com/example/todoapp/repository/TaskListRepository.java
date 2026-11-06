package com.example.todoapp.repository;

import com.example.todoapp.entity.TaskList;
import org.springframework.data.jpa.repository.JpaRepository;


public interface TaskListRepository extends JpaRepository<TaskList, Integer> {
}

