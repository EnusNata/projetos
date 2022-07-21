package dao;

import java.util.List;
import javabeans.Enfermaria;
import javax.persistence.Query;

public class EnfermariaDAO extends DataAccessObject {

    public EnfermariaDAO() {
        super(Enfermaria.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select E from Enfermaria E";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
