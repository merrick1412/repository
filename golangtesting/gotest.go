package main

import ("fmt"
	"time"
)
//unit of work
type Task struct {
    ID int
    Message string
}

func worker(id int, tasks <-chan Task, results chan<- string) {
    for task := range tasks {
	fmt.Printf("Worker %d started task %d\n", id, task.ID)
	time.Sleep(2 * time.Second) //sim work
	results <- fmt.Sprintf("Worker %d completed task %d: %s", id, task.ID, task.Message)

    }
}

func main() {
    numWorkers := 3
    numTasks := 5

    tasks := make(chan Task, numTasks)
    results := make(chan string, numTasks)//channels let tasks and results communicate

    //start workers
    for i := 1; i <= numWorkers; i++ {
        go worker(1,tasks,results) //threads
    }
    //give the tasks to them

    for i := 1; i <= numTasks; i++ {
         tasks <- Task{ID: i, Message: fmt.Sprintf("Task %d message", i)}
    }
    close(tasks)

    for i := 1; i <= numTasks; i++ {
        fmt.Println(<-results)
    }
}
