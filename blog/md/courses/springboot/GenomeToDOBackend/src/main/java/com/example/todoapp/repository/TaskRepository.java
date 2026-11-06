package com.example.todoapp.repository;

import com.example.todoapp.entity.Task;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;
import java.util.Optional;

public interface TaskRepository extends JpaRepository<Task, Integer> {
    @Query(
            nativeQuery = true,
            value = "SELECT task.t_id, task.completed, task.note, task.due_day, task.priority, task.title, task.list_id FROM task " +
                    "where task.t_id=:taskId")
    Optional<Task> findTaskByTaskId(@Param("taskId") Integer taskId);
}