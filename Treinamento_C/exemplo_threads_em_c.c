#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int count = 0;

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond_prod = PTHREAD_COND_INITIALIZER;
pthread_cond_t cond_cons = PTHREAD_COND_INITIALIZER;

void *produtor(void *arg) {
    for (int i = 0; i < 10; i++) {
        pthread_mutex_lock(&mutex);
        printf("[Produtor] Tentando produzir item %d...\n", i);
        
        while (count == BUFFER_SIZE) {
            printf("[Produtor] Buffer cheio! Aguardando consumidor...\n");
            pthread_cond_wait(&cond_prod, &mutex);
        }
        
        buffer[count] = i;
        printf("[Produtor] Produzido: %d\n", i);
        count++;
        
        pthread_cond_signal(&cond_cons);
        printf("[Produtor] Notificando consumidor.\n");
        pthread_mutex_unlock(&mutex);
        
        sleep(1);
    }
    return NULL;
}

void *consumidor(void *arg) {
    for (int i = 0; i < 10; i++) {
        pthread_mutex_lock(&mutex);
        printf("[Consumidor] Tentando consumir um item...\n");
        
        while (count == 0) {
            printf("[Consumidor] Buffer vazio! Aguardando produtor...\n");
            pthread_cond_wait(&cond_cons, &mutex);
        }
        
        int item = buffer[count - 1];
        printf("[Consumidor] Consumido: %d\n", item);
        count--;
        
        pthread_cond_signal(&cond_prod);
        printf("[Consumidor] Notificando produtor.\n");
        pthread_mutex_unlock(&mutex);
        
        sleep(2);
    }
    return NULL;
}

int main() {
    pthread_t t_prod, t_cons;
    
    printf("[Main] Criando threads produtor e consumidor...\n");
    pthread_create(&t_prod, NULL, produtor, NULL);
    pthread_create(&t_cons, NULL, consumidor, NULL);
    
    pthread_join(t_prod, NULL);
    pthread_join(t_cons, NULL);
    
    printf("[Main] Execução finalizada.\n");
    return 0;
}