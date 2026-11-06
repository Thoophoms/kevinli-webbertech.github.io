package com.example.todoapp.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.*;
import java.io.Serializable;
import java.time.LocalDateTime;

@Entity
@Data
@Builder
//@EqualsAndHashCode
@NoArgsConstructor
@AllArgsConstructor
public class Task implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @JsonProperty("id")
    private Integer tId;

    @Column(nullable = false)
    private String title;

    @JsonIgnore
    @Column(columnDefinition = "TEXT")
    private String note;

    @JsonProperty("DueDay")
    private LocalDateTime dueDay;

    @JsonIgnore
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private Priority priority;

    @Column(nullable = false)
    private Integer completed = 0;

    @ManyToOne
    @JoinColumn(name = "list_id")
    private TaskList taskList;
}
