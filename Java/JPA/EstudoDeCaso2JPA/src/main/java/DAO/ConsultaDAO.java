package dao;

import java.util.List;
import javabeans.Consulta;
import javax.persistence.Query;

public class ConsultaDAO extends DataAccessObject {

    public ConsultaDAO() {
        super(Consulta.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select C from Consulta C";
        Query query = this.manager.createQuery(jpql);
        return query.getResultList();
    }
    
}
