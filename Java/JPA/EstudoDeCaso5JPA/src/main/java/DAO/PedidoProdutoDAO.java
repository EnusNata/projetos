package DAO;

import javabeans.PedidoProduto;
import java.util.List;
import javax.persistence.Query;

/**
 *
 * @author Enus
 */
public class PedidoProdutoDAO extends DataAccessObject {

    public PedidoProdutoDAO(){
        super(PedidoProduto.class);
    }
    
    @Override
    public List listar(Object obj) {
        String jpql = "select P from PedidoProduto P";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
