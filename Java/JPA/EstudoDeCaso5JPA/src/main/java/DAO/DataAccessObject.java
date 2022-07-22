package DAO;

import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

/**
 *
 * @author Enus
 */
public abstract class DataAccessObject<T> {
    
    private Class type;
    
    protected EntityManager manager;

    public DataAccessObject(Class type) {
        this.type = type;
        
        EntityManagerFactory factory = Persistence.createEntityManagerFactory("EstudoDeCaso5JPA_PU");
        this.manager = factory.createEntityManager();    
    }
    
    public boolean salvar(T obj){
        
        EntityTransaction transaction = this.manager.getTransaction();
        
        try {
            
            transaction.begin();
            obj = (T) this.manager.merge(obj);
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
            
            T obj = (T) this.manager.find(this.type, id);
            
            return obj;
            
        } catch (Exception e) {
            
            return null;
        }
    }
    
    public abstract List listar(T obj);
}
