package com.example.todoapp.controller;

//import com.example.todoapp.TaskList;
//import com.example.todoapp.TaskListService;
import com.example.todoapp.entity.TaskList;
import com.example.todoapp.service.TaskListService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/v1")
public class TaskListController {

    @Autowired
    private TaskListService taskListService;

    @GetMapping("/tasklists")
    public List<TaskList> getAllTaskLists() {
        return taskListService.getAllTaskLists();
    }

    @GetMapping("/tasklist/{id}")
    public TaskList getAllTaskLists(@PathVariable int id) {
        return taskListService.getTaskListById(id);
    }

    @PostMapping("/tasklist")
    public TaskList createTaskList(@RequestBody TaskList taskList) {
        return taskListService.saveTaskList(taskList);
    }

    @DeleteMapping("/tasklist/{id}")
    public void deleteTaskList(@PathVariable Integer id) {
        taskListService.deleteTaskList(id);
    }
}


