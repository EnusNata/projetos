package dao;

import javabeans.Voo;
import java.util.List;
import javax.persistence.Query;

public class VooDAO extends DataAccessObject {

    public VooDAO() {
        super(Voo.class);
    }

    @Override
    public List listar() {
        String jpql = "select V from Voo V";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
