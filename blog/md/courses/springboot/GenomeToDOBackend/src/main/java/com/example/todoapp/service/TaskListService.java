package com.example.todoapp.service;

//import com.example.todoapp.TaskList;
//import com.example.todoapp.TaskListRepository;

import com.example.todoapp.entity.TaskList;
import com.example.todoapp.repository.TaskListRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class TaskListService {

    @Autowired
    private TaskListRepository taskListRepository;

    public List<TaskList> getAllTaskLists() {
        return taskListRepository.findAll();
    }

    public TaskList getTaskListById(int id) {
        return taskListRepository.getReferenceById(id);
    }

    public TaskList saveTaskList(TaskList taskList) {
        return taskListRepository.save(taskList);
    }

    public void deleteTaskList(Integer id) {
        taskListRepository.deleteById(id);
    }
}