#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <stdio.h>
#include "hashtable.h"


#define INIT_CAPACITY 100

struct node{
	char *key;
	int type;
	int address;
	int inicializada;
};


struct hashtable {
	struct node **table;
	unsigned int capacity;	
	unsigned int num_elems;
};



static unsigned int hash(HashTable h, char *key)
{
	int hash = 7, i;
	for ( i = 0; i < strlen(key); i++) {
    	hash = hash*31 + key[i];
	}
	return hash%(h->capacity);

}

static HashTable increaseHashTable(HashTable h)
{
	h->capacity *= 2;

	h->table = realloc(h->table, sizeof(struct node*) * h->capacity);

	assert(h->table != NULL);

	return h;
}


static HashTable calcAlpha(HashTable h) 
{
	double a = 0;

	if (h != NULL && h->table != NULL) {
		a = ((double) (h->num_elems / h->capacity));

		if (a >= 0.8) {
			h = increaseHashTable(h);
		}
	}

	return h;
}

HashTable createHashTable(const unsigned int capacity)
{
	unsigned int i = 0;
	HashTable h = malloc(sizeof(struct hashtable));

	if (h == NULL) {
		h = realloc(h, sizeof(struct hashtable));
		assert(h != NULL);
	}

	h->capacity = (capacity == 0) ? INIT_CAPACITY : capacity;
	h->num_elems = 0;

	h->table = malloc(sizeof(struct node*) * h->capacity);

	if (h->table == NULL) {
		h->table = realloc(h->table, sizeof(struct node*) * h->capacity);
		assert(h->table != NULL);
	}

	for (i=0; i < h->capacity; i++) {
		h->table[i] = NULL;
	}

	return h;
}


void destroyHashTable(HashTable h) {
	unsigned int i = 0;

	if (h != NULL) {
		if (h->table != NULL) {
			for (; i < h->capacity; i++) {
				if (h->table[i] != NULL) {
					h->table[i] = NULL;
				}
			}
			
			free(h->table);
			h->table = NULL;
		}

		free(h);		
		h = NULL;
	}
}


HashTable addHashTable(HashTable h,char *key, int address, int tipo)
{
	unsigned int index = 0;

	if (h != NULL && h->table != NULL) {
		index = hash(h, key);

		if (h->table[index] == NULL) 
		{
			h->num_elems++;
			h->table[index] = malloc(sizeof(*h->table[index]));
			h->table[index]->address = address;
			h->table[index]->type = tipo;
			h->table[index]->inicializada = 1;
			h->table[index]->key = (char *) malloc(strlen(key)+1);
			strcpy(h->table[index]->key,key);
			h = calcAlpha(h);
			return h;
		}
	}
	return h;
	
}

table get_HashTable(HashTable hashtbl, char *key)
{
	table node;
	int index=hash(hashtbl,key);
	node=hashtbl->table[index];
	if(node!=NULL) {
		if(!strcmp(node->key, key)) return node;
	}

	return NULL;
}


int getEndereco(const HashTable h, char *key){
	table aux;
	aux = get_HashTable(h,key);
	return aux->address;
}



int getInicializacao(const HashTable h, char *key){
	table aux;
	aux = get_HashTable(h,key);
	return aux->inicializada;
}

int getType(const HashTable h, char *key){
	table aux;
	aux = get_HashTable(h,key);
	return aux->type;
}