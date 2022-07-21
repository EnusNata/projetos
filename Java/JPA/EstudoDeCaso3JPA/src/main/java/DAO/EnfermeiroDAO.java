package dao;

import java.util.List;
import javabeans.Enfermeiro;
import javax.persistence.Query;

public class EnfermeiroDAO extends DataAccessObject {

    public EnfermeiroDAO() {
        super(Enfermeiro.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select E from Enfermeiro E";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
