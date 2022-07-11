package DAO;

import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

public abstract class DataAcessObject<T> {
    
    protected EntityManager manager;
    private Class type;
    
    public DataAcessObject(Class type){
        EntityManagerFactory factory = Persistence.createEntityManagerFactory("EstudoDeCaso1-PU");
        this.manager = factory.createEntityManager();
        this.type = type;
    }
    
    public boolean salvar(T obj){
        EntityTransaction transaction = this.manager.getTransaction();
        
        try {
            transaction.begin();
            obj = this.manager.merge(obj);
            transaction.commit();
            
            return true;
        } catch (Exception e) {
            transaction.rollback();
            
            return false;
        }
    }
    
    public boolean remover(long id){
        EntityTransaction transaction = this.manager.getTransaction();
        
        try {
            transaction.begin();
            T obj = (T) this.manager.find(this.type, id);
            this.manager.remove(obj);
            transaction.commit();
            
            return true;
        } catch (Exception e) {
            transaction.rollback();
            
            return false;
        }
    }
    
    public T abrir(long id){
        try {
            T obj = (T) this.manager.find(this.type,id);
            return obj;
        } catch (Exception e) {
            return null;
        }
    }
    
    public abstract List<T> listar(T obj);
}