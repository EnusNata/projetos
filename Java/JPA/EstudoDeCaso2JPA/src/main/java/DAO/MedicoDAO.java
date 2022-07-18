package dao;

import java.util.List;
import javabeans.Medico;
import javax.persistence.Query;

public class MedicoDAO extends DataAccessObject{

    public MedicoDAO() {
        super(Medico.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select M from Medico M";
        Query query = this.manager.createQuery(jpql);
        return query.getResultList();
    }
    
    
}
