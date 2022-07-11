package DAO;

import java.util.List;
import javabeans.Departamento;
import javax.persistence.Query;

public class DepartamentoDAO extends DataAcessObject{

    public DepartamentoDAO() {
        super(Departamento.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select D from Departamento D";
        Query query = this.manager.createNamedQuery(jpql);
        return query.getResultList();
    }
    
}
