package dao;

import java.util.List;
import javabeans.Alocacao;
import javax.persistence.Query;

public class AlocacaoDAO extends DataAccessObject{

    public AlocacaoDAO() {
        super(Alocacao.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select A from Alocacao A";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
