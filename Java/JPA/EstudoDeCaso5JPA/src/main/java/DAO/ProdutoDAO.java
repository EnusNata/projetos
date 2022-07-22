package DAO;

import javabeans.Produto;
import java.util.List;
import javax.persistence.Query;

/**
 *
 * @author Enus
 */
public class ProdutoDAO extends DataAccessObject {

    public ProdutoDAO(){
        super(Produto.class);
    }
    
    @Override
    public List listar(Object obj) {
        String jpql = "select P from Produto P";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
